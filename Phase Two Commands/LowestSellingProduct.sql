SELECT TOP 1 productData.product_name
FROM salesData
INNER JOIN productData ON productData.product_id = salesData.product_id
GROUP BY product_name 
ORDER BY SUM(quantity_sold) ASC;
