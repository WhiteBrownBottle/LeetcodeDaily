select IFNULL((select e1.Name from Employee as e1, Employee as e2
    where e1.ManagerId=e2.Id and e1.Salary>e2.Salary), Null) as Employee