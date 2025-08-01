## Setup
```
Create an Azure AI Foundry resource
	We’ll grant your user identity the Azure AI User role so you can develop with all projects under this resource.
	Your data is encrypted by default using Microsoft-managed keys.
	Go to Azure AI Foundry portal
	... More
	My Assets -> Models + endpoints
	Model deployments
	Deploy Model -> Deploy base Model
	Select gpt-4.1-mini
	Confirm
	Deploy gpt-4.1-mini
		Deployment type: Global standard
		Model Version: 2025-04-14
		Resource  Location: East US 2
	Create resource and deploy
	
		Endpoint
		Target URI:
		Authentication type Key:
```
### Run code_generation.py
```
(azure) C:\project\Week1\05.code_generation>python code_generation.py
### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### A query to list the names of the departments which employed more than 10 employees in the last 3 months
```
	query:
```sql
SELECT d.name
FROM Department d
JOIN Employee e ON d.id = e.department_id
JOIN Salary_Payments sp ON e.id = sp.employee_id
WHERE sp.date >= CURRENT_DATE - INTERVAL '3 months'
GROUP BY d.id, d.name
HAVING COUNT(DISTINCT e.id) > 10
```

### Run code_generation_2.py
```
(azure) C:\project\Week1\05.code_generation>python code_generation_2.py
The given SQL query retrieves the names of departments that have more than 10 employees who have received salary payments in the last 3 months.

Here's a step-by-step explanation:

1. **FROM Department d JOIN Employee e ON d.id = e.department_id**
   This joins the `Department` table with the `Employee` table, linking each employee to their respective department.

2. **WHERE e.id IN (SELECT employee_id FROM Salary_Payments WHERE date > now() - interval '3 months')**
   This filters the employees to only those who have salary payment records within the last 3 months.

3. **GROUP BY d.name**
   The results are grouped by department name.

4. **HAVING COUNT(*) > 10**
   Only departments with more than 10 such employees are included in the final result.

**In summary:**
The query lists department names where more than 10 employees have been paid salaries in the past 3 months.
```
