using System.ComponentModel;

namespace AhorcadoDjango;

public partial class MainPage : ContentPage, INotifyPropertyChanged
{
    private int count = 0;
    private string status = "HOLA";
    private string spotLight = "_ _ _";
    private List<char> letters = new List<char>();
    private string message = "Mensaje";
    private int mistakes = 0;
    private int maxWrong = 5;
    private string currentImage = "error0.png";
    private string currentQuestion;
    private string answer = "";
    private List<char> guessed = new List<char>();

    public int Count
    {
        get => Count;
        set
        {
            count = value;
            OnPropertyChanged();
        }
    }

    public string Status
    {
        get => status;
        set
        {
            status = value;
            OnPropertyChanged();
        }
    }

    public string SpotLight
    {
        get => spotLight;
        set
        {
            spotLight = value;
            OnPropertyChanged();
        }
    }

    public List<char> Letters
    {
        get => letters;
        set
        {
            letters = value;
            OnPropertyChanged();
        }
    }

    public string Message
    {
        get => message;
        set
        {
            message = value;
            OnPropertyChanged();
        }
    }

    public string CurrentImage
    {
        get => currentImage;
        set
        {
            currentImage = value;
            OnPropertyChanged();
        }
    }

    public string CurrentQuestion
    {
        get => currentQuestion;
        set
        {
            currentQuestion = value;
            OnPropertyChanged();
        }
    }


    List<(string Question, string Answer)> djangoQuestions = new List<(string, string)>()
    {
        ("Framework web para desarrollar en Python", "Django"),
        ("¿Lenguaje principal?", "Python"),
        ("¿Almacena datos?", "Models"),
        ("¿Conjunto de objetos?", "Queryset"),
        ("¿Configuración principal?", "Settings"),
        ("¿Cómo se llama el archivo de migraciones?", "Migrations"),
        ("¿Para qué sirve 'admin.py'?", "Admin"),
        ("¿Patrón de diseño utilizado?", "MTV"),
        ("¿Cómo se llaman las plantillas en Django?", "Templates"),
        ("¿Elemento para manejar URLs?", "Urls"),
        ("¿Cómo se denomina el script de inicialización?", "Manage"),
        ("¿Objetos para pasar datos a las plantillas?", "Context"),
        ("¿Tipo de relación uno a uno?", "OneToOne"),
        ("¿Cómo se llama la interfaz de usuario administrativa?", "Admin"),
        ("¿Comando para iniciar un proyecto?", "Startproject"),
    };


    public MainPage()
    {
        InitializeComponent();
        Letters.AddRange("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ");
        BindingContext = this;
        Pickword();
        CalcularPalabra(answer, guessed);
    }

    private void Pickword()
    {
        var random = new Random();
        var selectedPair = djangoQuestions[random.Next(djangoQuestions.Count)];
        var selectedQuestion = selectedPair.Question;
        answer = selectedPair.Answer.ToUpper();
        CurrentQuestion = selectedQuestion;
    }

    private void CalcularPalabra(string answer, List<char> guessed)
    {
        var temp = answer.Select(x => (guessed.IndexOf(x) >= 0 ? x : '_')).ToArray();
        SpotLight = string.Join(' ', temp);
    }

    private void OnCounterClicked(object sender, EventArgs e)
    {
        count++;
        Status = "HOLA " + count;
    }

    void btnReiniciar_Clicked(System.Object sender, System.EventArgs e)
    {
        mistakes = 0;
        guessed = new List<char>();
        Message = "";
        CurrentImage = "dotnet_bot.png";
        Pickword();
        CalcularPalabra(answer, guessed);
        actualizarStatus();
        habilitarLetras();
    }

    void Button_Clicked(System.Object sender, System.EventArgs e)
    {
        var btn = sender as Button;
        if (btn != null)
        {
            var letter = btn.Text;
            btn.IsEnabled = false;
            HandleGuess(letter[0]);
        }
    }

    private void HandleGuess(char letter)
    {
        if (guessed.IndexOf(letter) == -1)
        {
            guessed.Add(letter);
        }
        if (answer.IndexOf(letter) >= 0)
        {
            CalcularPalabra(answer, guessed);
            ganado();
        }
        else if (answer.IndexOf(letter) == -1)
        {
            mistakes++;
            actualizarStatus();
            perdido();
        }
    }

    private void perdido()
    {
        if (mistakes == maxWrong)
        {
            Message = "PERDISTE!";
            deshabilitarLetras();
        }
    }

    private void ganado()
    {
        if (SpotLight.Replace(" ", "") == answer)
        {
            Message = "GANASTE!";
            deshabilitarLetras();
        }
    }

    private void deshabilitarLetras()
    {
        foreach (var c in Contenedor.Children)
        {
            var btn = c as Button;
            if (btn != null)
            {
                btn.IsEnabled = false;
            }
        }
    }

    private void habilitarLetras()
    {
        foreach (var c in Contenedor.Children)
        {
            var btn = c as Button;
            if (btn != null)
            {
                btn.IsEnabled = true;
            }
        }
    }

    private void actualizarStatus()
    {
        Status = $"Errores: {mistakes} de {maxWrong}";
        CurrentImage = $"error{mistakes}.png";
    }
}