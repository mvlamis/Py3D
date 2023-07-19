import unittest
from main import SoftwareRender

class TestSoftwareRender(unittest.TestCase):
    def setUp(self):
        self.sr = SoftwareRender()

    def test_screen_size(self):
        self.assertEqual(self.sr.WIDTH, 800)
        self.assertEqual(self.sr.HEIGHT, 600)

    def test_camera_position(self):
        self.assertEqual(self.sr.camera.position, [0, 0, -10])

    def test_object_faces(self):
        self.assertEqual(len(self.sr.object.faces), 24)

if __name__ == '__main__':
    unittest.main()