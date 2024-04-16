**Example 1: BatchForceSuccessIntegrationTaskInstances**



Input: 

```
tccli wedata BatchForceSuccessIntegrationTaskInstances --cli-unfold-argument  \
    --ProjectId abc \
    --Instances.0.TaskId 123 \
    --Instances.0.CurRunDate 2022-04-12 17:00:15 \
    --Instances.1.TaskId 1234 \
    --Instances.1.CurRunDate 2022-04-12 18:00:15
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "abc"
    }
}
```

