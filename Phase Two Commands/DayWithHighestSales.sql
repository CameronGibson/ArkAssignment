SELECT TOP 1 salesData.sales_date
FROM salesData
GROUP BY salesData.sales_date
ORDER BY SUM(salesData.quantity_sold) DESC;