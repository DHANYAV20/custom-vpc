import aws_cdk as core
import aws_cdk.assertions as assertions

from custom_vpc.custom_vpc_stack import CustomVpcStack

# example tests. To run these tests, uncomment this file along with the example
# resource in custom_vpc/custom_vpc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CustomVpcStack(app, "custom-vpc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
