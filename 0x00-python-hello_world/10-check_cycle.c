#include "lists.h"

/**
 * check_array: Check array for number
 * @num: Number passed
 * @ar: Array to check
 *
 * Return: 1 - if num is present
 *         0 - otherwise
 */
int check_array(int num, int *ar)
{
	int i;

	for (i = 0; i < 10; i++)
	{
		if (num == ar[i])
		{
			return (1);
		}
	}
	return (0);
}


/**
 * check_cycle - check if there is a loop in linked list(a cycle)
 * @list: Pointer to linked list
 *
 * Return: 0 - If there is no cycle
 *         1 - if there is cycle
 */
int check_cycle(listint_t *list)
{
	int ar[200] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1}, i = 0;

	while (list != NULL)
	{
		if (check_array(list->n, ar) == 1)
			return (1);
		ar[i] = list->n;
		list = list->next;
		i++;
	}
	return (0);
}
