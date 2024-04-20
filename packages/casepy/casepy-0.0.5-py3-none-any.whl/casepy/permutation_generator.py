from .simple_methods import *
import random


class PermutationGenerator:

    def __init__(self):
        self.element_list_initialized = False
        self.number_of_selection_initialized = False

    def set_parameters(self, in_number_of_selection: int, element_list: list):
        self.in_number_of_selection = in_number_of_selection
        self.element_list = element_list

        self.element_list_initialized = True
        self.number_of_selection_initialized = True
        self.max_possible = permutation(len(element_list), in_number_of_selection)

    def possible_cases(self):
        return self.max_possible

    def all_case(self) -> list:
        if not self.element_list_initialized:
            raise Exception("element_list is not initialized")
        if not self.number_of_selection_initialized:
            raise Exception("number_of_selection is not initialized")

        result_list = []
        for i in range(self.max_possible):
            result_list.append(
                self.permutation_core(i, self.in_number_of_selection, self.element_list)
            )
        return result_list

    def random_case(self, return_i=False) -> list:
        if not self.element_list_initialized:
            raise Exception("element_list is not initialized")
        if not self.number_of_selection_initialized:
            raise Exception("number_of_selection is not initialized")

        random_i = (int)(random.random() * self.max_possible)

        if return_i:
            return random_i, self.permutation_core(
                random_i,
                self.in_number_of_selection,
                self.element_list,
            )
        return self.permutation_core(
            random_i,
            self.in_number_of_selection,
            self.element_list,
        )

    def i_case(self, in_iterator: int) -> list:
        if not self.element_list_initialized:
            raise Exception("element_list is not initialized")
        if not self.number_of_selection_initialized:
            raise Exception("number_of_selection is not initialized")

        return self.permutation_core(
            in_iterator, self.in_number_of_selection, self.element_list
        )

    def permutation_core(
        self, in_iterator: int, in_number_of_selection: int, element_list: list
    ) -> list:
        result_list = []
        buff_element_list = element_list.copy()
        number_of_element = len(buff_element_list)

        for i in range(in_number_of_selection):
            current_permutation = permutation(
                number_of_element - i - 1, in_number_of_selection - i - 1
            )
            current_permutation_index = in_iterator // current_permutation
            in_iterator = in_iterator % current_permutation
            result_list.append(buff_element_list[current_permutation_index])
            buff_element_list.pop(current_permutation_index)

        return result_list
