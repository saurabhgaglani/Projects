using UnityEngine;

public class PlayerMovement : MonoBehaviour
{

    public float moveSpeed; 
    private Animator anim;
    private bool IsMoving;
    private Vector2 MoveDir;
    private bool isAttacking;
    public float attackTime;
    private float attackTimeCounter;
    private Rigidbody2D myRigidbody;

    // Start is called before the first frame update
    void Start()
    {

        anim = GetComponent<Animator>();
        myRigidbody = GetComponent<Rigidbody2D>();
        
    }

    // Update is called once per frame
    void Update()
    {
        IsMoving = false;

        if (!isAttacking)
        {
            if (Input.GetAxisRaw("Horizontal") > 0 || Input.GetAxisRaw("Horizontal") < 0)
            {
                transform.Translate(new Vector3(Input.GetAxisRaw("Horizontal") * moveSpeed * Time.deltaTime, 0f, 0f));
                MoveDir = new Vector2(Input.GetAxisRaw("Horizontal"), 0f);
                IsMoving = true;
            }

            else if (Input.GetAxisRaw("Vertical") < 0 || Input.GetAxisRaw("Vertical") > 0)
            {
                transform.Translate(new Vector3(0f, Input.GetAxisRaw("Vertical") * moveSpeed * Time.deltaTime, 0f));
                MoveDir = new Vector2(0f, Input.GetAxisRaw("Vertical"));
                IsMoving = true;
            }



            if (Input.GetKeyDown(KeyCode.J))
            {
                attackTimeCounter = attackTime;
                isAttacking = true;
                myRigidbody.velocity = Vector2.zero;
                anim.SetBool("isAttacking", true);

            }
        }

        if (attackTimeCounter > 0)
        {
            attackTimeCounter -= Time.deltaTime;
        }
        else
        {
            isAttacking = false;
            anim.SetBool("isAttacking", false);
        }


        anim.SetFloat("MoveX", Input.GetAxisRaw("Horizontal"));
        anim.SetFloat("MoveY", Input.GetAxisRaw("Vertical"));
        anim.SetBool("PlayerMoving", IsMoving);
        anim.SetFloat("LastMoveX", MoveDir.x);
        anim.SetFloat("LastMoveY", MoveDir.y);

    
    }
}
