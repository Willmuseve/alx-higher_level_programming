#include "lists.h"

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Points to the first element of the list.
 * Return: 1 if the list is palindrome, otherwise 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int array[4096];
	int list = 0, half_size = 0, i = 0;

	if (!head)
		return (1);

	current = *head;
	while (current)
	{
		array[list] = current->n;
		current = current->next;
		list++;
	}

	list--;
	half_size = list / 2;

	for (i = 0; i <= half_size; i++, list--)
	{
		if (array[i] != array[list])
			return (0);
	}

	return (1);
}
