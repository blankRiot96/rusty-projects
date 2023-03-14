use crossterm::{cursor, terminal, ExecutableCommand, QueueableCommand};
use std::io::{stdout, Write};
use std::{thread, time};

fn main() {
    let mut stdout = stdout();

    stdout.execute(cursor::Hide).unwrap();
    for i in (1..30).rev() {
        stdout.queue(cursor::SavePosition).unwrap();
        stdout
            .write_all(format!("{}: FOOBAR \n", i).as_bytes())
            .unwrap();
        stdout.queue(cursor::RestorePosition).unwrap();
        stdout.flush().unwrap();
        stdout.queue(cursor::SavePosition).unwrap();
        stdout
            .write_all(format!("{}: FOOBAR ", i * 2).as_bytes())
            .unwrap();
        stdout.queue(cursor::RestorePosition).unwrap();
        stdout.flush().unwrap();
        thread::sleep(time::Duration::from_millis(500));

        stdout.queue(cursor::RestorePosition).unwrap();
        stdout
            .queue(terminal::Clear(terminal::ClearType::FromCursorDown))
            .unwrap();
    }
    stdout.execute(cursor::Show).unwrap();

    println!("Done!");
}
