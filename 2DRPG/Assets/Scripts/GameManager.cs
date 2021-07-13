using UnityEngine.SceneManagement;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public GameOverScript gameOver;
    bool gamehasended = false;
    public void Endgame()
    {
        if (!gamehasended)
        {
            gamehasended = true;
            gameOver.Setup();
        }
    }



}
