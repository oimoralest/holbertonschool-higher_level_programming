#include "lists.h"
/**
 *list_len - returns the number of elements in a linked list_t list
 *@h: list
 *
 *Return: n number of elements in @h
 */
size_t list_len(const listint_t *h)
{
	size_t n = 0;
	const listint_t *ptr;

	ptr = h;
	while (ptr)
		ptr = ptr->next, n++;

	return (n);
}
/**
 *get_nodeint_at_index - returns the nth node of a listint_t list
 *@head: head of the list
 *@index: nth node to search
 *
 *Return: NULL if the node does not exist or address of the nth node
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int counter = 0;

	while (head && counter < index)
		head = head->next, counter++;

	return (head);
}
/**
 * is_palindrome - checks if a singly list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux, *aux2;
	unsigned int len = 0;

	if (!head || !*head)
		return (1);
	if (!(*head)->next)
		return (1);
	len = list_len(*head);
	aux = *head;
	aux2 = get_nodeint_at_index(*head, --len);
	while (aux->n == aux2->n)
	{
		if (aux->next == aux2 || aux->next->next == aux2)
			return (1);
		aux = aux->next;
		aux2 = get_nodeint_at_index(*head, --len);
	}

	return (0);
}
