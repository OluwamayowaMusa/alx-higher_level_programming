#include "lists.h"

/**
 * reverse_list - Reverse linked list
 * @head: Pointer to pointer in linked list
 *
 * Return: Reverse linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current, *old = NULL, *list;

	list = *head;
	while (list)
	{
		current = list->next;
		list->next = old;
		old = list;
		list = current;
	}
	*head = old;
	return (*head);
}

/**
 * is_palindrome - Check if linked list is a palindrome
 * @head: Pointer to pointer to linked list
 *
 * Return: 1 - if is palindrome
 *         0 - if is not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL, *revNode = NULL, *freeNode = NULL;
	size_t numNode, i = 0;
	int res = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (numNode = 0, temp = *head; temp != NULL; numNode++, temp = temp->next)
		;
	temp = *head;
	while (i < numNode / 2)
		temp = temp->next, i++;
	revNode = reverse_list(&temp);
	freeNode = revNode;
	temp = *head;
	while (temp->next->next != NULL)
		temp = temp->next;
	temp->next = NULL;
	temp = *head;
	while (revNode)
	{
		if (revNode->n != temp->n)
		{
			res = 0;
			break;
		}
		revNode = revNode->next;
		temp = temp->next;
	}
	free_listint(freeNode);
	return (res);
}
