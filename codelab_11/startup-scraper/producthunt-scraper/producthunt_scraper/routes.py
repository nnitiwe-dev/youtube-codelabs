from crawlee.crawlers import PlaywrightCrawlingContext
from crawlee.router import Router
from datetime import datetime

router = Router[PlaywrightCrawlingContext]()


@router.default_handler
async def default_handler(context: PlaywrightCrawlingContext) -> None:
    """Main handler for scraping Product Hunt products."""

    context.log.info(f'Processing {context.request.url} ...')
    page = context.page
    products = []

    # Wait for the page to load completely
    await page.wait_for_load_state('networkidle')
    
    # Wait for product cards to be visible
    try:
        await page.wait_for_selector('[data-test="homepage-section-0"]', timeout=10000)
    except:
        print("Could not find main product section, trying alternative selectors...")
    
    # Find all product elements using Playwright selectors
    product_elements = await page.query_selector_all('div[data-test*="post-item"], .styles_item__Dk_nz, [data-test*="post"]')
    
    if not product_elements:
        # Fallback selectors
        product_elements = await page.query_selector_all('div:has(h3), article, .post-item')
    
    print(f"Found {len(product_elements)} product elements")
    
    # Process each product element
    for index, element in enumerate(product_elements):
        try:
            # Get product name
            name_element = await element.query_selector('h3, [data-test*="post-name"], a strong, strong')
            name = await name_element.inner_text() if name_element else None
            
            # Get product description  
            desc_element = await element.query_selector('p, [data-test*="post-description"], .description')
            description = await desc_element.inner_text() if desc_element else None
            
            # Get vote count
            vote_element = await element.query_selector('[data-test*="vote-button"], button span, .vote-count')
            votes = None
            if vote_element:
                vote_text = await vote_element.inner_text()
                vote_match = vote_text.strip()
                if vote_match.isdigit():
                    votes = int(vote_match)
                else:
                    # Extract number from text like "123 votes"
                    import re
                    vote_nums = re.findall(r'\d+', vote_match)
                    if vote_nums:
                        votes = int(vote_nums[0])
            
            # Get product URL/link
            link_element = await element.query_selector('a[href*="/posts/"], a[href*="producthunt.com/posts/"]')
            product_url = None
            if link_element:
                href = await link_element.get_attribute('href')
                if href:
                    product_url = href if href.startswith('http') else f'https://www.producthunt.com{href}'
            
            # Get maker/creator info
            maker_element = await element.query_selector('[data-test*="maker"], .maker, .author')
            maker = await maker_element.inner_text() if maker_element else None
            
            # Get product image/logo
            img_element = await element.query_selector('img')
            image_url = await img_element.get_attribute('src') if img_element else None
            
            # Only push data if we have a valid product name
            if name and name.strip():
                await context.push_data({
                    'scraped_url': context.request.loaded_url,
                    'scraped_at': datetime.now().isoformat(),
                    'rank': index + 1,
                    'name': name.strip(),
                    'description': description.strip() if description else None,
                    'votes': votes,
                    'product_url': product_url,
                    'maker': maker.strip() if maker else None,
                    'image_url': image_url
                })
                
                # Log progress
                print(f"{index + 1}. {name.strip()} - {votes if votes else 'N/A'} votes")
                products.append({
                    'rank': index + 1,
                    'name': name.strip(),
                    'votes': votes
                })
                
        except Exception as e:
            print(f"Error processing product element {index + 1}: {e}")
            continue
