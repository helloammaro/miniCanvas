import pytest
from course import Course, CourseManager
import unittest


@pytest.fixture
def course_instance():
    return Course(1, "COSC381", "Winter 2024", ["Teacher1", "Teacher2"])

@pytest.fixture
def course_manager_instance():
    return CourseManager()

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course_id = 1
        self.course_code = "COSC177"
        self.semester = "Winter"
        self.teacher_list = ["Jane Doe", "Jon Smith"]
        self.student_list = ["Alice", "Bob"]
        self.course = Course(self.course_id, self.course_code, self.semester, self.teacher_list)

    def test_course_init(self):
        course = self.course
        
        # Assert that attributes are initialized correctly
        self.assertEqual(course.course_id, 1)
        self.assertEqual(course.course_code, "COSC177")
        self.assertEqual(course.semester, "Winter")
        self.assertEqual(course.teacher_list, ["Jane Doe", "Jon Smith"])
        self.assertEqual(course.student_list, [])
        self.assertEqual(course.assignment_list, [])
        self.assertEqual(course.module_list, [])
        self.assertEqual(course.assignment_counter, 0)

    def test_import_students_method(self):
        course = self.course
        students = ["Student1", "Student2"]
        course.import_students(students)
        
        
        self.assertEqual(course.student_list, students)

    def test_create_an_assignment_method(self):
        
        course = self.course
        due_date = "2077-07-07"
        course.create_an_assignment(due_date)
        
        
        self.assertEqual(len(course.assignment_list), 1)
        self.assertEqual(course.assignment_list[0].due_date, due_date)
        self.assertEqual(course.assignment_list[0].course_id, 1)

    def test_generate_assignment_id_method(self):
        course = self.course
        self.assertEqual(course.generate_assignment_id(), 1)
        self.assertEqual(course.generate_assignment_id(), 2)

    def test_validate_teacher_list_method(self):
        course = self.course
        self.assertTrue(course.validate_teacher_list())

        course.teacher_list.append(123)
        self.assertFalse(course.validate_teacher_list())

    def test_validate_student_list_method(self):
        course = self.course
        self.assertTrue(course.validate_student_list())

        course.student_list.append(456)
        self.assertFalse(course.validate_student_list())

if __name__ == '__main__':
    unittest.main()