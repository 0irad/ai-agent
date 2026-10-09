import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):

    def test_current_dir(self) -> None:
        result = get_files_info("calculator", ".")
        print("Result for current directory:\n\t")
        print(result)
        # self.assertEqual(result, 'Success: "." is within the working directory')

    def test_bin_dir(self) -> None:
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:\n\t")
        print(result)
        # self.assertEqual(
        #     result,
        #     'Error: Cannot list "/bin" as it is outside the permitted working directory',
        # )

    def test_parent_dir(self) -> None:
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:\n\t")
        print(result)
        # self.assertEqual(
        #     result,
        #     'Error: Cannot list "../" as it is outside the permitted working directory',
        # )

    def test_main_file(self) -> None:
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:\n\t")
        print(result)
        # self.assertEqual(
        #     result,
        #     'Error: "main.py" is not a directory',
        # )


if __name__ == "__main__":
    unittest.main()
