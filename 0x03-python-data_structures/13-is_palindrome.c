#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: Pointer to pointer to linked list
 *
 * Return: 1 - if palindrome
 *         0 - if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL, *temp2 = NULL;
	int numNode, first = 0, last, i, j;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	for (numNode = 0; temp != NULL; temp = temp->next, numNode++)
		;
	last = numNode;
	while (first < numNode / 2 && last > numNode / 2)
	{
		temp = temp2 = *head;
		for (i = 0; i < first; temp = temp->next, i++)
			;
		for (j = 0; j < last - 1; temp2 = temp2->next, j++)
			;
		if (temp->n != temp2->n)
			return (0);
		first++, last--;
	}
	return (1);
}
