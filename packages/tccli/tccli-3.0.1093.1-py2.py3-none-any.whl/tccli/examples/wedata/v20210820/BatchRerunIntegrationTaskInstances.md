**Example 1: BatchRerunIntegrationTaskInstances**



Input: 

```
tccli wedata BatchRerunIntegrationTaskInstances --cli-unfold-argument  \
    --ProjectId 123456 \
    --Instances.0.TaskId 123 \
    --Instances.0.CurRunDate 2022-04-12 17:00:15 \
    --Instances.1.TaskId 1234 \
    --Instances.1.CurRunDate 2022-04-12 18:00:15
```

Output: 
```
{
    "Response": {
        "TaskNames": [
            "abc"
        ],
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "12345"
    }
}
```

