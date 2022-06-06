#include "lists.h"

/**
 * add_nodeint - add node to linked list
 * @head: pointer to pointer to linked list
 * @n: Data
 *
 * Return: Address of new Node
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t  *newNode = NULL;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;
	return (newNode);
}


/**
 * is_palindrome - Checks if a linked list is a panlindrome
 * @head: Pointer to pointer to linked List
 *
 * Return: 0 - if not a palindrome
 *         1 - if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *storeNode = NULL, *temp, *temp1, *temp2, *temp3;
	int ctrl = 1, i = 0, j = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	temp = temp1 = temp3 = *head;
	while (temp3 != NULL)
		temp3 = temp3->next, i++;
	if (i % 2 != 0)
		return (0);
	while (temp != NULL && temp->next != NULL)
	{
		if (temp->n == (temp->next)->n && j == (i / 2) - 1)
		{
			temp = temp->next;
			break;
		}
		temp = temp->next, j++;
	}
	while (temp != NULL)
		add_nodeint(&storeNode, temp->n), temp = temp->next;
	temp2 = storeNode;
	while (storeNode != NULL)
	{
		if (temp1->n != storeNode->n)
		{
			ctrl = 0;
			break;
		}
		storeNode = storeNode->next, temp1 = temp1->next;
	}
	free_listint(temp2);
	return (ctrl);
}
