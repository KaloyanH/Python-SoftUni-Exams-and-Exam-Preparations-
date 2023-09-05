from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):

    def setUp(self) -> None:
        self.report = StudentReportCard("Test1", 12)

    def test_correct_innit(self):
        self.assertEqual("Test1", self.report.student_name)
        self.assertEqual(12, self.report.school_year)
        self.assertEqual({}, self.report.grades_by_subject)

    def test_student_name_prop(self):
        with self.assertRaises(ValueError) as ve:
            self.report.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_student_success_name(self):
        self.report.student_name = "K"
        self.assertEqual("K", self.report.student_name)


    def test_school_year_prop_below_1(self):
        with self.assertRaises(ValueError) as ve:
            self.report.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_prop_above_12(self):
        with self.assertRaises(ValueError) as ve:
            self.report.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_successful_year(self):
        self.report.school_year = 1

        self.assertEqual(1, self.report.school_year)

    def test_add_grade_if_not_present_returns_success(self):
        self.report.grades_by_subject = {"Pesho": [6.5, 6.5]}
        self.report.add_grade("Koko", 8.5)

        self.assertEqual({"Pesho": [6.5, 6.5], "Koko": [8.5]}, self.report.grades_by_subject)

    def test_add_grade_if_present_and_empty_grades_returns_success(self):
        self.report.grades_by_subject = {"Pesho": [], "Koko": [8.5]}
        self.report.add_grade("Pesho", 8.5)

        self.assertEqual({"Pesho": [8.5], "Koko": [8.5]}, self.report.grades_by_subject)

    def test_add_grade_if_student_is_present(self):
        self.report.grades_by_subject = {"Koko": [8.5], "Pesho": [6.5, 6.5]}

        self.report.add_grade("Koko", 6.2)

        self.assertEqual({"Koko": [8.5, 6.2], 'Pesho': [6.5, 6.5]}, self.report.grades_by_subject)

    def test_report_average_grade_by_subject(self):
        self.report.grades_by_subject = {"Koko": [8.5, 8.5], "Pesho": [5.5, 5.5]}

        result = self.report.average_grade_by_subject()
        self.assertEqual("Koko: 8.50\nPesho: 5.50", result)
        self.assertEqual({"Koko": [8.5, 8.5], "Pesho": [5.5, 5.5]}, self.report.grades_by_subject)

    def test_average_grade_for_all_students(self):
        self.report.grades_by_subject = {"Koko": [5.5, 5.5], "Pesho": [5.5, 5.5], "Misho": [5.5, 5.5]}

        result = self.report.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.50", result)
        self.assertEqual({"Koko": [5.5, 5.5], "Pesho": [5.5, 5.5], "Misho": [5.5, 5.5]}, self.report.grades_by_subject)


    def test_repr_method(self):
        self.report.grades_by_subject = {"Koko": [5.5, 5.5], "Pesho": [5.5, 5.5]}
        self.assertEqual(f"Name: Test1\n"
                         f"Year: 12\n"
                         f"----------\n"
                         f"Koko: 5.50\n"
                         f"Pesho: 5.50\n"
                         f"----------\n"
                         f"Average Grade: 5.50", self.report.__repr__())


if __name__ == "__main__":
    main()
