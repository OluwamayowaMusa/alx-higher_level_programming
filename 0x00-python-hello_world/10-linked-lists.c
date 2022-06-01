#include "lists.h"

/**
 * print_listint - Prints the contents of linked list
 * @h: Pointer to linked list
 *
 * Return: Number of nodes
 */
size_t print_listint(const listint_t *h)
{
	size_t i = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		i++;
		h = h->next;
	}
	return (i);
}


/**
 * add_nodeint - add node to linked list
 * @head: Pointer to pointer to linked list
 * @n: New data
 *
 * Return: New linked list
 *
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newNode;

	if (head == NULL)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;

	return (newNode);
}

/**
 * free_listint - free the linked list
 * @head: Pointer to linked list
 *
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head->next;
		free(head);
		head = current;
	}
}
