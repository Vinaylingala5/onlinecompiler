from rest_framework import generics, status
from rest_framework.response import Response
from .models import Submission
from .serializers import SubmissionSerializer
from problems.models import Problem
import requests
import time

JUDGE0_URL = "https://judge0-ce.p.rapidapi.com/submissions"

class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     problem_id = self.request.data.get("problem")
    #     code = self.request.data.get("code")
    #     language = self.request.data.get("language")

    #     problem = Problem.objects.get(id=problem_id)
    #     testcases = problem.test_cases

    #     all_passed = True
    #     total_runtime = 0.0
    #     verdict = "AC"  # ✅ default verdict

    #     for tc in testcases:
    #         start_time = time.time()

    #         payload = {
    #             "source_code": code,
    #             "language_id": self._get_lang_id(language),
    #             "stdin": tc["input"],
    #             "expected_output": tc["output"],
    #         }

    #         response = requests.post(f"{JUDGE0_URL}?base64_encoded=false&wait=true", json=payload)
    #         result = response.json()

    #         if result.get("status", {}).get("description") != "Accepted":
    #             all_passed = False
    #             verdict = result.get("status", {}).get("description")
    #             break

    #         total_runtime += (time.time() - start_time)

    #     final_verdict = "AC" if all_passed else verdict

    #     serializer.save(
    #         user=user,
    #         verdict=final_verdict,
    #         runtime=round(total_runtime, 3)
    #     )
        

    # def _get_lang_id(self, lang):
    #     """Map language to Judge0 language ID"""
    #     mapping = {
    #         "python": 71,
    #         "java": 62,
    #         "cpp": 54
    #     }
    #     return mapping.get(lang, 71)
