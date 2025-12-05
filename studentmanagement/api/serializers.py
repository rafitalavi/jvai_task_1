from rest_framework import serializers
from student.models import Student 
from course.models import Course   
from results.models import Result 


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
class ResultSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='subject.name' , read_only = True)
    class Meta:
        model = Result
        fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many = True , read_only = True)
    avg_marks = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = "__all__"
    def get_avg_marks(self, obj):
        results = obj.results.all()
        if results.exists():
            total_marks = sum(result.marks_obtained for result in results)
            avg = total_marks / results.count()
            return round(avg , 2)
            # if avg:
            #     if 79 <=avg < 100:
            #         return "A+"
            #     elif 79 <= avg < 60:
            #         return "A"
            #     elif 60 <= avg < 50:
            #         return "B"
            #     elif 50 <= avg < 40:
            #         return "C"
            #     else:
            #         return "F"
        return 0
class StudentResultSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True, read_only=True)
    avg_marks = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields =  "__all__"
        # Added 'id' to fields
    
    def get_avg_marks(self, obj):
        results = obj.results.all()
        if results.exists():
            total_marks = sum(result.marks_obtained for result in results)
            avg = total_marks / results.count()
            return round(avg, 2)
        return 0
    
    def get_grade(self, obj):
        avg = self.get_avg_marks(obj)
        print("Average Marks:", avg)  # Debugging line
        if avg == 0:
            return "N/A"
        if 80 <= avg <= 100:
            return "A+"
        elif 70 <= avg < 80:
            return "A"
        elif 60 <= avg < 70:
            return "B"
        elif 50 <= avg < 60:
            return "C"
        else:
            return "F"
        