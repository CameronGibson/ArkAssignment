SELECT TOP 1 salesmanData.salesman_name
FROM salesData
INNER JOIN salesmanData ON salesmanData.salesman_id = salesData.salesman_id
WHERE sales_date BETWEEN '2020-11-01' AND '2020-11-30'
GROUP BY salesman_name
ORDER BY SUM(quantity_sold) DESC;
