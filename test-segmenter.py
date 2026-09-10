from io import StringIO
import subprocess
import unittest
from segmenter import *

class TestSegmenter(unittest.TestCase):

    list_of_lists = [["one", "two", "three", "."], 
                     ["one", "two", "three", "four", "?"],
                     ["one", "two", "!"],
                     ["one", "two", "three", "four", "five", ";"]]
    
    def testMyBestSegmenter(self):
        """ Check that your my_best_segmenter has the right interface """

        tokens = sum(self.list_of_lists, [])
        out = my_best_segmenter(tokens)
        self.assertEqual(type(out), list, msg="<strong>Problem with my_best_segmenter</strong><br/>The function my_best_segmenter should return a list, but it is returning a {}".format(str(type(out))))

        for e in out: 
            self.assertEqual(type(e), list, msg="<strong>Problem with my_best_segmenter</strong></br>The elements in the list returned by my_best_segmenter should be lists, but {} is a {}".format(e, str(type(e))))
            for s in e:
                self.assertEqual(type(s), str, msg="<strong>Problem with my_best_segmenter</strong><br/>The elemnets in the list of lists returned by my_best_segmenter should be strings, but {} is a {}.".format(s, str(type(s))))

    def testWriteSentenceBoundaries(self):
        """ Check that your write_sentence_boundaries function works """

        expected = '3\n8\n11\n17\n'
        output = StringIO()
        write_sentence_boundaries(self.list_of_lists, output)
        self.assertEqual(output.getvalue(), expected)

    def testMainInterface(self):
        """ Check that the main segmenter interface interface works """

        command = ["python", "segmenter.py", "-t", "/courses/cs159/data/brown-hidden/adventure.txt", "-y", "test_suite_out.txt"]
        subprocess.run(command, capture_output=True)
        try: 
            fp = open("test_suite_out.txt", "r")
        except:
            self.fail(msg="<strong>Problem with segmenter.py</strong><br/>Your segmenter.py does not generate a file with the name passed with -y")
        try: 
            lines = [int(x.strip()) for x in fp.readlines()]
        except: 
            self.fail(msg="<strong>Problem with segmenter.py</strong><br/>Your segmenter.py does not generate ints on each line.")

if __name__ == '__main__':
    unittest.main()