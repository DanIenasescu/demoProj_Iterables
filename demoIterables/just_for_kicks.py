def search_simple(el_to_search_for):
    # list of animals
    Animals= ["cat", "dog", "tiger"]
    if el_to_search_for in Animals:
        # searching positiion of dog
        print(Animals.index(el_to_search_for))
        return [Animals.index(el_to_search_for), el_to_search_for]
    else:
        print("Element not in list")
        return [-1, "el not found"]


print(search_simple("dog"))
