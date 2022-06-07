#include "lists.h"

/**
 * print_listint - print all Elements in linked list
 * @h: Pointer to linked list
 *
 * Return: Number of nodes
 */
size_t print_listint(const listint_t *h)
{
	size_t i = 0;

	while (h != NULL)
	{
		printf("%d %p\n", h->n, (void *)h);
		i++;
		h = h->next;
	}
	return (i);
}


/**
 * add_nodeint_end - adds node at the end of a linked list
 * @head: Pointer of first node of linked list
 * @n: integer to be included in new node
 *
 * Return: address of the new element of NULL if it fails
 *
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *newNode = NULL, *temp;

	if (head == NULL)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	temp = *head;
	while (temp->next != NULL)
		temp = temp->next;
	temp->next = newNode;
	return (newNode);
}


/**
 * free_listint - Free linked list
 * @head: Pointer to the linked list
 *
 */
void free_listint(listint_t *head)
{
	listint_t *current = NULL;

	while (head != NULL)
	{
		current = head->next;
		free(head);
		head = current;
	}
}
