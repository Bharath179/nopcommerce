import os

def test_save_screenshot(driver, test_name):
    # Ensure screenshots folder exists
    screenshot_folder = ".\\screenshots"
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)

    # Save the screenshot
    screenshot_path = os.path.join(screenshot_folder, f"{test_name}.png")
    print(f"Saving screenshot to: {screenshot_path}")
    driver.save_screenshot(screenshot_path)