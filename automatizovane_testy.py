import pytest
from playwright.sync_api import Page, expect


URL = "https://www.pluxee.cz/"


# Test 1: Ověření titulku stránky
def test_page_title(page: Page):
    """Stránka musí mít v titulku slovo 'Pluxee'."""
    page.goto(URL)
    expect(page).to_have_title(pytest.approx("Pluxee", rel=0))  # fallback níže
    assert "Pluxee" in page.title(), f"Očekáváno 'Pluxee' v titulku, ale nalezeno: '{page.title()}'"


# Test 2: Ověření viditelnosti loga
def test_logo_is_visible(page: Page):
    """Logo Pluxee musí být na stránce viditelné."""
    page.goto(URL)
    logo = page.locator("img[alt='Pluxee']")
    expect(logo).to_be_visible()


# Test 3: Ověření funkčnosti navigačního odkazu „Zaměstnavatelé"
def test_employers_navigation_link(page: Page):
    """Kliknutí na odkaz 'Zaměstnavatelé' musí změnit URL nebo načíst příslušnou stránku."""
    page.goto(URL)
    # Klikneme na první přímý odkaz v menu vedoucí na stránku pro zaměstnavatele
    link = page.locator("a[href*='stravenky-zamestnavatel']").first
    expect(link).to_be_visible()
    link.click()
    expect(page).to_have_url("https://www.pluxee.cz/stravenky-zamestnavatel/")
