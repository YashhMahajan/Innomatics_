from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Sample products data
products = [
    {"product_id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics"},
    {"product_id": 2, "name": "Notebook", "price": 99, "category": "Stationery"},
    {"product_id": 3, "name": "USB Hub", "price": 799, "category": "Electronics"},
    {"product_id": 4, "name": "Pen Set", "price": 49, "category": "Stationery"},
]

# Sample orders data
orders = [
    {"order_id": 1, "customer_name": "Rahul Sharma", "product": "Wireless Mouse"},
    {"order_id": 2, "customer_name": "Alice Johnson", "product": "Notebook"},
    {"order_id": 3, "customer_name": "Rahul Kumar", "product": "USB Hub"},
]

@app.get("/products/search")
def search_products(keyword: str = Query(...)):
    results = [p for p in products if keyword.lower() in p['name'].lower()]
    if not results:
        return {"message": f"No products found for: {keyword}"}
    return {"total_found": len(results), "products": results}


@app.get("/products/sort")
def sort_products(sort_by: str = Query("price"), order: str = Query("asc")):
    if sort_by not in ["price", "name"]:
        return {"error": "sort_by must be 'price' or 'name'"}
    
    reverse = True if order == "desc" else False
    sorted_products = sorted(products, key=lambda p: p[sort_by], reverse=reverse)
    return sorted_products


@app.get("/products/page")
def paginate_products(page: int = Query(1), limit: int = Query(2)):
    start = (page - 1) * limit
    end = start + limit
    paginated_products = products[start:end]
    total_pages = -(-len(products) // limit)  # Ceiling division
    return {"page": page, "total_pages": total_pages, "products": paginated_products}


@app.get("/orders/search")
def search_orders(customer_name: str):
    results = [o for o in orders if customer_name.lower() in o['customer_name'].lower()]
    if not results:
        return {"message": f"No orders found for: {customer_name}"}
    return {"customer_name": customer_name, "total_found": len(results), "orders": results}


@app.get("/products/sort-by-category")
def sort_by_category():
    sorted_products = sorted(products, key=lambda p: (p['category'], p['price']))
    return {"products": sorted_products}


@app.get("/products/browse")
def browse_products(keyword: str = Query(None), sort_by: str = Query("price"), order: str = Query("asc"), page: int = Query(1), limit: int = Query(4)):
    result = products
    if keyword:
        result = [p for p in result if keyword.lower() in p['name'].lower()]
    
    if sort_by in ["price", "name"]:
        result = sorted(result, key=lambda p: p[sort_by], reverse=(order == "desc"))
    
    total_found = len(result)
    total_pages = -(-total_found // limit)
    start = (page - 1) * limit
    paged_result = result[start:start + limit]
    
    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total_found": total_found,
        "total_pages": total_pages,
        "products": paged_result,
    }