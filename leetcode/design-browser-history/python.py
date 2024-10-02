class Page:
    def __init__(self, homepage, prev=None, next=None):
        self.homepage = homepage
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.currPage = Page(homepage)

    def visit(self, url: str) -> None:
        self.currPage.next = Page(url, self.currPage)
        self.currPage = self.currPage.next

    def back(self, steps: int) -> str:
        while self.currPage.prev and steps != 0:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.homepage

    def forward(self, steps: int) -> str:
        while self.currPage.next and steps != 0:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.homepage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
