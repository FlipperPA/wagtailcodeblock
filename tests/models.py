def test_home_page_with_code_block(home_page, client):
    """
    Checks to make sure we can create a page with a code block.
    """
    print(home_page)

    assert "for x" in home_page.body
