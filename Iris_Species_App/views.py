from django.shortcuts import render
import pickle

# Create your views here.

def home(request):

    return render(request, 'home.html')

def result(request):

    print("--->",request)

    if request.method == "GET":

        print("Iris POST -> ",request.method)

        sepal_len = float(request.GET.get('sepal_length'))
        sepal_wid = float(request.GET.get('sepal_width'))
        petal_len = float(request.GET.get('petal_length'))
        petal_wid = float(request.GET.get('petal_width'))

        model = pickle.load(open('iris_model.pkl','rb'))

        new_prediction = model.predict(
            [[sepal_len, sepal_wid, petal_len, petal_wid]]
        )

    return  render(request, 'result.html', {'result':new_prediction[0]})

