import requests
from bs4 import BeautifulSoup
import time
import os
from openpyxl import Workbook

def crawl_naver_search_results(search_keyword, total_pages=100):
    wb = Workbook()
    ws = wb.active
    ws.append(["Blog Title", "Blog URL", "Posting Date"])

    for page in range(1, total_pages+1):
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={((page-1)*10)+1}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            blog_results = soup.select(".sh_blog_top")
            if not blog_results:
                print(f"No results found on page {page}.")
                break

            print(f"Results from page {page}:")
            for blog in blog_results:
                blog_url = blog.select_one(".sh_blog_title").get("href")
                blog_title = blog.select_one(".sh_blog_title").get("title")
                blog_posting_date = blog.select_one(".txt_inline").get_text()
                print(f"Blog Title: {blog_title}")
                print(f"Blog URL: {blog_url}")
                print(f"Posting Date: {blog_posting_date}\n")

                ws.append([blog_title, blog_url, blog_posting_date])

            # Add a delay to avoid overloading the server
            time.sleep(1)

        else:
            print(f"Failed to fetch search results on page {page}. Status code: {response.status_code}")

    save_folder = "c:\\work"
    os.makedirs(save_folder, exist_ok=True)
    save_file_path = os.path.join(save_folder, f"{search_keyword}_search_results.xlsx")
    wb.save(save_file_path)
    print(f"Search results saved to {save_file_path}")

if __name__ == "__main__":
    search_keyword = input("Enter the search keyword: ")
    crawl_naver_search_results(search_keyword)
