import datetime
import unittest
import os
from fnmatch import fnmatch

import time
import logging
import asyncio
from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.models.blocks import SectionBlock, DividerBlock

logging.basicConfig(level=logging.INFO)

ENABLE_SLACK_OUTPUT = True

load_dotenv()

SLACK_TOKEN = os.getenv('SLACK_TOKEN')

def extract_test_name(test_case):
    """
    Extracts and returns the docstring of a test method from a given test case.
    If no docstring is available, returns the method name.

    :param test_case: The test case object containing the test method
    :return: The docstring or method name of the test
    """
    method_name = test_case.id().split('.')[-1]
    test_method = getattr(test_case, method_name, None)
    return test_method.__doc__.strip() if test_method and test_method.__doc__ else method_name

async def send_slack_message(has_failures, test_result, total_time):
    """
    Asynchronously sends a detailed test report to a Slack channel using blocks.
    

    :param has_failures: Boolean indicating if there are any failures
    :param test_result: The unittest test result object
    :param total_time: Float representing total time taken for tests
    """
    if not ENABLE_SLACK_OUTPUT:
        # Log the message to console instead of sending it to Slack
        logging.info("\nSending Slack message is disabled. Logging message to console instead.\n")
        logging.info("Summary of Test Results:")
        logging.info(f"Ran {test_result.testsRun} tests in {total_time:.2f} seconds.")
        logging.info(f"{len(test_result.errors)} Errors, {len(test_result.failures)} Failures.\n")
        return

    client = AsyncWebClient(token=SLACK_TOKEN)
    blocks = [SectionBlock(text=f"*API Test Execution Report*").to_dict(), DividerBlock().to_dict()]

    # Construct message based on test results
    if test_result.wasSuccessful() and not has_failures:
        blocks.append(SectionBlock(text=f"*✅ All tests passed!*").to_dict())

    if has_failures:
        blocks.append(SectionBlock(text="*Test Failures:*").to_dict())
        for test_case, _ in test_result.failures:
            method_name = test_case.id().split('.')[-1]
            test_method = getattr(test_case, method_name)
            test_name = test_method.__doc__ or method_name
            failure_reason = getattr(test_case, 'failure_reason', 'Failure reason not captured')
            blocks.append(SectionBlock(text=f"Test Name: {test_name}\nOutcome: ❌ Failure\nReason: {failure_reason}").to_dict())

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary_text = f"*Testing Results Summary:*\nRan {test_result.testsRun} tests in {total_time:.2f} seconds.\n{len(test_result.errors)} Errors, {len(test_result.failures)} Failures.\nTest Run Time: {current_datetime}"
    blocks.append(SectionBlock(text=summary_text).to_dict())

    try:
        response = await client.chat_postMessage(channel='#configure-alerts', blocks=blocks, text="API Test Execution Report - See Slack for detailed results.")
        if response["ok"]:
            logging.info("Message sent successfully to Slack.")
        else:
            logging.error(f"Failed to send message to Slack. Error: {response['error']}")
    except SlackApiError as e:
        logging.error(f"Error occurred while sending message to Slack: {e.response['error']}")

def import_tests():
    """
    Dynamically imports test modules from the 'src/tests' directory and adds them to a test suite.

    :return: A unittest.TestSuite object containing all loaded tests
    """
    test_suite = unittest.TestSuite()
    current_directory = os.path.dirname(__file__)
    tests_directory = os.path.join(current_directory, "src", "funcytests")

    for file_name in os.listdir(tests_directory):
        if fnmatch(file_name, "test_*.py"):
            module_path = f"src.funcytests.{file_name[:-3]}"
            
            try:
                # Import the module dynamically
                module = __import__(module_path, fromlist=[''])
                
                # Add the tests from the module to the test suite
                test_suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))
            except ImportError as e:
                logging.error(f"Failed to import {module_path}: {e}")

    return test_suite

async def main():
    """
    Main function to execute the test suite, collect results, and send a detailed report to Slack.
    """
    runner = unittest.TextTestRunner(verbosity=1)
    start_time = time.time()
    test_result = runner.run(import_tests())
    end_time = time.time()
    total_time = end_time - start_time

    detailed_results = ""
    for test_case, outcome in test_result.failures + test_result.errors:
        reason = outcome[1] if isinstance(outcome, tuple) else "Unknown reason"
        emoji = '❌' if 'Fail' in reason else ''
        detailed_results += f"\n\nTest Name: {test_case.id()}\nOutcome: {emoji} {reason}\n"

    detailed_results += f"\n\nRan {test_result.testsRun} tests in {total_time:.2f} seconds."
    detailed_results += f"\n{len(test_result.errors)} Errors, {len(test_result.failures)} Failures."
    has_failures = len(test_result.failures) > 0

    await send_slack_message(has_failures, test_result, total_time)

if __name__ == "__main__":
    asyncio.run(main())
