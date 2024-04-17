from test_retriever_from_md_file import test_retriever_from_md_file
from test_runnable_from_md_file import test_runnable_from_md_file
from test_retriever_from_url import test_retriever_from_url
from test_runnable_from_url import test_runnable_from_url

def main():

    # Load environment variables
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    md_file_path = "src/retriever/md/leave_policy.md"
    url = "https://python.langchain.com/docs/langsmith/"

    try:
        test_retriever_from_md_file(md_file_path)
    except AssertionError as e:
        print(f"✘ Test failed: {e}")

    try:
        test_runnable_from_md_file(md_file_path)
    except AssertionError as e:
        print(f"✘ Test failed: {e}")

    try:
        test_retriever_from_url(url)
    except AssertionError as e:
        print(f"✘ Test failed: {e}")

    try:
        test_runnable_from_url(url)
    except AssertionError as e:
        print(f"✘ Test failed: {e}")

if __name__ == "__main__":
    main()
