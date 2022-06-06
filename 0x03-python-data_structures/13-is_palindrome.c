#include "lists.h"

/**
 * num_list - Check if linked list contain the same value
 * @list: Pointer to linked list
 *
 * Return: 1 - same value
 *         0 - otehrwise
 */
int num_list(listint_t *list)
{
	int value;

	value = list->n;
	while (list != NULL)
	{
		if (list->n != value)
			return (0);
		list = list->next;
	}
	return (1);
}

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
	listint_t *storeNode = NULL, *temp, *temp1, *temp2, *temp3, *temp4;
	int ctrl = 1, i = 0, j = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	temp = temp1 = temp3 = temp4 = *head;
	while (temp3 != NULL)
		temp3 = temp3->next, i++;
	if (num_list(temp4) == 1)
		return (1);
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
