#!/usr/bin/python3
"""A Module printing the posts from JSON holder"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them as a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        posts_data = [{
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]} for post in posts]

        filename = "posts.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)
        print(f"Posts saved to {filename}")
    else:
        print("Failed to fetch posts.")
