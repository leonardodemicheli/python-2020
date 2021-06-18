from unittest import TestCase
from file import File


class TestFile(TestCase):
    f = File("free_Space.txt")

    def test_count_lines(self):
        self.assertEqual(3, self.f.count_lines())

    def test_count_letters(self):
        self.assertEqual(2, self.f.count_letters('o'))

    def test_copy_file(self):
        self.f.copy_file('test.txt')
        with open(self.f.filePath, 'r') as reader:
            file1 = reader.readlines()
        with open('test.txt', 'r') as reader:
            file2 = reader.readlines()
        self.assertEqual(file1, file2)
