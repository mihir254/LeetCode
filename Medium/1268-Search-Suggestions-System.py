class Solution:
    def suggestedProducts(self, products, searchWord):
        # Brute Force
        products.sort()
        suggestions = []
        for i in range(1, len(searchWord)+1):
            current_word = searchWord[:i]
            suggestion = []
            for product in products:
                if len(suggestion) < 3:
                    if product[:i] == current_word:
                        suggestion.append(product)
            suggestions.append(suggestion)
        return suggestions