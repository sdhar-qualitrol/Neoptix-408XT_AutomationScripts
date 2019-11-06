import time
import junit_xml

TEST_TIME = time.time()

class TestCase(junit_xml.TestCase):
  def __init__(self, name, classname=None, elapsed_sec=None, stdout=None, stderr=None):
        global TEST_TIME
        if elapsed_sec == 0:
            if TEST_TIME > 0:
                elapsed_sec = time.time() - TEST_TIME
        junit_xml.TestCase.__init__(self, name, classname, elapsed_sec, stdout, stderr)
        TEST_TIME = time.time()

