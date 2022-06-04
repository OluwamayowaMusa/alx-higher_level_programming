#include "lists.h"

/**
 * print_listint - Print the data in a linked list
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
		h = h->next;
		i++;
	}
	return (i);
}


/**
 * add_nodeint_end - Add node to linked list
 * @head: Pointer to Head Node
 * @n: Data
 *
 * Return: pointer to new node
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *newNode = NULL, *temp;

	if (head == NULL)
		return  (NULL);
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
 * @head: Pointer to linked list
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
