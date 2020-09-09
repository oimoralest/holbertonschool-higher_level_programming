#include "lists.h"
/**
 *is_palindrome - return if a string is palindrome
 *@s: pointer to the string
 *
 *Return: 1 if is palindrome
 *        0 if is not
 */

int is_palindrome_buffer(char *s)
{
	char *fp;

	fp = final_position(s);

	return (palindrome(s, fp));
}

/**
 *final_position - returns a pointer to the final position of a string
 *@s: pointer to the string
 *
 *Return: fp final position of the string
 */

char *final_position(char *s)
{
	return (*s == '\0' ? (s - 1) : final_position(s + 1));
}

/**
 *palindrome - check if a string is palindrome or not
 *@s: pointer to the initial position of the string
 *@fp: pointer to the final position of the string
 *
 *Return: 1 if is palindrome
 *        0 if is not
 */

int palindrome(char *s, char *fp)
{
	return (*s != *fp ? 0 : s == fp || s > fp ? 1 :
		palindrome(s + 1, fp - 1));
}
/**
 * is_palindrome - checks if a singly list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux;
	char buffer[100000];
	unsigned int i = 0, _ret = 0;

	if (!head || !*head)
		return (1);
	if (!(*head)->next)
		return (1);
	aux = *head;
	while (aux)
	{
		buffer[i] = aux->n + '0';
		aux = aux->next, i++;
	}
	buffer[i] = '\0';
	_ret = is_palindrome_buffer(buffer);

	return (_ret);
}
