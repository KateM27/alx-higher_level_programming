#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_palindrome - checks if the list is palindrome
 * @head: ptr to the beginning of the list
 * @last: ptr to the end of the list
 * Return: 0 if not palindrome, else 1
 */
int check_palindrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - calls check_palindrome
 * @head: ptr to beginning of the list
 * Return: 0 if not palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}
