#include "lists.h"

/**
 * add_nodeint - add node to the end of linked list
 * @head: Pointer to pointer to linked list
 * @n: Data
 *
 * Return: Address of linked list
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newNode = NULL;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;
	return (newNode);
}

/**
 * is_panlindrome - check if a linked list is palindrome
 * @head: Pointer to pointer to linked list
 *
 * Return: 1 - if palindrome
 *         0 - if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *storeNode = NULL, *temp = NULL, *temp1 = NULL;
	int res = 1;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		add_nodeint(&storeNode, temp->n);
		temp = temp->next;
	}
	temp1 = storeNode;
	temp = *head;
	while (storeNode != NULL && temp != NULL)
	{
		if (storeNode->n != temp->n)
		{
			res = 0;
			break;
		}
		storeNode = storeNode->next;
		temp = temp->next;
	}
	free_listint(temp1);
	return (res);
}
