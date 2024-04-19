from .simple_methods import combination
import random


class CombinationGenerator:

    def __init__(self):
        self.element_list_initialized = False
        self.number_of_selection_initialized = False

    def set_parameters(self, in_number_of_selection: int, element_list: list):
        self.in_number_of_selection = in_number_of_selection
        self.element_list = element_list

        self.element_list_initialized = True
        self.number_of_selection_initialized = True
        self.max_possible = combination(len(element_list), in_number_of_selection)

    def all_case(self) -> list:
        if not self.element_list_initialized:
            raise Exception("element_list is not initialized")
        if not self.number_of_selection_initialized:
            raise Exception("number_of_selection is not initialized")

        result_list = []
        for i in range(self.max_possible):
            result_list.append(
                self.combination_core(i, self.in_number_of_selection, self.element_list)
            )
        return result_list

    def random_case(self, return_i=False) -> list:
        if not self.element_list_initialized:
            raise Exception("element_list is not initialized")
        if not self.number_of_selection_initialized:
            raise Exception("number_of_selection is not initialized")

        random_i = (int)(random.random() * self.max_possible)

        if return_i:
            return random_i, self.combination_core(
                random_i,
                self.in_number_of_selection,
                self.element_list,
            )
        return self.combination_core(
            random_i,
            self.in_number_of_selection,
            self.element_list,
        )

    def i_case(self, in_iterator: int) -> list:
        if not self.element_list_initialized:
            raise Exception("element_list is not initialized")
        if not self.number_of_selection_initialized:
            raise Exception("number_of_selection is not initialized")

        return self.combination_core(
            in_iterator, self.in_number_of_selection, self.element_list
        )

    # def combination_case(self, in_iterator: int, in_number_of_selection: int) -> list:
    #     if self.element_list_initialized:
    #         raise Exception("element_list is not initialized")
    #     return self.combination_case(
    #         in_iterator, in_number_of_selection, self.element_list
    #     )

    def combination_core(
        self, in_iterator: int, in_number_of_selection: int, element_list: list
    ) -> list:
        result_list = []
        number_of_elements = len(element_list)
        max_possible = combination(number_of_elements, in_number_of_selection)

        if in_iterator >= max_possible:
            return []

        target_iterator = 0
        while True:
            if in_number_of_selection == 0:
                break

            test = combination(number_of_elements - 1, in_number_of_selection - 1)

            if in_iterator >= test:
                in_iterator -= test

                number_of_elements -= 1

                target_iterator += 1

            else:
                result_list.append(element_list[target_iterator])

                number_of_elements -= 1
                in_number_of_selection -= 1

                target_iterator += 1

        return result_list


if __name__ == "__main__":
    generator = CombinationGenerator()
    generator.set_parameters(4, [1, 2, 3, 4, 5])

    print(generator.all_case())
