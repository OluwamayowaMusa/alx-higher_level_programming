#include "lists.h"

/**
 * insert_node - insert number in a sorted linked list
 * @head: Pointer to pointer to head node
 * @number: Number to be inserted
 *
 * Return: Address of new Node or Node if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *newNode = NULL, *temp1 = NULL;

	if (head == NULL)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	if (*head == NULL)
	{
		newNode->next = NULL;
		*head = newNode;
		return (newNode);
	}
	if (number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	temp1 = *head;
	while (temp1->next != NULL)
	{
		if (temp1->next->n < number)
			temp1 = temp1->next;
		else
			break;
	}
	if (temp1->next == NULL)
	{
		newNode->next = NULL;
		temp1->next = newNode;
		return (newNode);
	}
	temp = temp1->next;
	newNode->next = temp;
	temp1->next = newNode;
	return (newNode);
}
