from playwright.sync_api import Page,expect


def test_UICheck(page:Page):
    #hide / display and placeholder locator
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()

    #Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role('link',name="Top").click()

    #Frame Handling
    pageFrame = page.frame_locator('#courses-iframe')
    pageFrame.get_by_role('link', name="All Access Plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")

    #Check the price of rice is equal to 37
    #1. identify the price column
    #2. identify the rice row
    #3. extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # get the index of the price column
    print(page.locator('th').count())
    for index in range(page.locator('th').count()):
       if page.locator('th').nth(index).filter(has_text="Price").count()>0:
           colValue = index
           #print(f"Index of price column value: {colValue}")
           break

    # check the rice price
    # my solution -
    # assert int(page.locator('tr').filter(has_text='Rice').locator('td').nth(colValue).text_content()) == 37
    # his solution
    riceRow = page.locator('tr').filter(has_text='Rice')
    expect(riceRow.locator('td').nth(colValue)).to_have_text("37")
