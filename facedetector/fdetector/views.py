import boto3
from django.conf import settings
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class FaceDetectorView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, fortmat=None):
        if "file" not in request.data:
            return Response("No file found", status=status.HTTP_400_BAD_REQUEST)
        image_file = request.data["file"]
        client = boto3.client(
            "rekognition",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
        )
        image = {"Bytes": image_file.read()}
        try:
            result = client.detect_faces(Image=image, Attributes=["DEFAULT"])
        except client.exceptions.InvalidS3ObjectException:
            return Response(
                "InvalidS3ObjectException", status=status.HTTP_400_BAD_REQUEST
            )
        except client.exceptions.InvalidParameterException:
            return Response(
                "InvalidParameterException", status=status.HTTP_400_BAD_REQUEST
            )
        except client.exceptions.ImageTooLargeException:
            return Response(
                "ImageTooLargeException", status=status.HTTP_400_BAD_REQUEST
            )
        except client.exceptions.AccessDeniedException:
            return Response("AccessDeniedException", status=status.HTTP_400_BAD_REQUEST)

        except client.exceptions.InternalServerError:
            return Response("InternalServerError", status=status.HTTP_400_BAD_REQUEST)

        except client.exceptions.ThrottlingException:
            return Response("ThrottlingException", status=status.HTTP_400_BAD_REQUEST)
        except client.exceptions.ProvisionedThroughputExceededException:
            return Response(
                "ProvisionedThroughputExceededException",
                status=status.HTTP_400_BAD_REQUEST,
            )
        except client.exceptions.InvalidImageFormatException:
            return Response(
                "InvalidImageFormatException",
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "result": True if len(result["FaceDetails"]) > 0 else False,
            },
            status=status.HTTP_200_OK,
        )
