from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_innit(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_if_shelf_doesnt_exist_raise_exception(self):
        self.store.toy_shelf = {"A": "toy",
                                "B": "book",
                                "C": "bike"}

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("D", "ship")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({"A": "toy",
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)

    def test_add_toy_if_toy_name_exists_raise_exception(self):
        self.store.toy_shelf = {"A": "toy",
                                "B": "book",
                                "C": "bike"}

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "toy")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual({"A": "toy",
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)

    def test_add_toy_if_toy_is_not_none_raise_exception(self):
        self.store.toy_shelf = {"A": "toy",
                                "B": "book",
                                "C": "bike"}

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "cooler")

        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertEqual({"A": "toy",
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)

    def test_add_toy_if_success(self):
        self.store.toy_shelf = {"A": None,
                                "B": "book",
                                "C": "bike"}

        result = self.store.add_toy("A", "pen")
        self.assertEqual("Toy:pen placed successfully!", result)
        self.assertEqual({"A": "pen",
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)

    def test_remove_toy_if_shelf_doesnt_exist_raise_exception(self):
        self.store.toy_shelf = {"A": "toy",
                                "B": "book",
                                "C": "bike"}

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("D", "car")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({"A": "toy",
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)

    def test_remove_toy_if_toy_is_not_on_the_shelf_raise_exception(self):
        self.store.toy_shelf = {"A": "toy",
                                "B": "book",
                                "C": "bike"}

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "pen")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual({"A": "toy",
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)

    def test_remove_toy_if_success(self):
        self.store.toy_shelf = {"A": "toy",
                                "B": "book",
                                "C": "bike"}

        result = self.store.remove_toy("A", "toy")
        self.assertEqual("Remove toy:toy successfully!", result)
        self.assertEqual({"A": None,
                          "B": "book",
                          "C": "bike"}, self.store.toy_shelf)


if __name__ == "__main__":
    main()
