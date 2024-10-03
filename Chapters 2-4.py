# Combine all flashcards for chapters 2, 3, and 4 into a single dataset for export to CSV

flashcards_chapter_2_4 = {
    "Question": [
        # Chapter 2
        "What are the Four Stages of Competence?",
        "What does 'front-loading your learning' mean?",
        "Why is learning by doing important?",
        "What is timeboxing, and how does it help?",
        "What are effective strategies for asking questions?",
        "What is impostor syndrome?",
        "What is the Dunning-Kruger effect?",
        "How should engineers approach feedback?",
        "What does 'conscious incompetence' mean?",
        "Why are side projects important?",

        # Chapter 3
        "What is technical debt?",
        "What is the 'Legacy Code Change Algorithm'?",
        "Why should code be left cleaner than you found it?",
        "What are incremental changes in code?",
        "What is pragmatic refactoring?",
        "What are version control best practices?",
        "What is the danger of 'going rogue' in a team setting?",
        "Why is it important to write tests for legacy code before making changes?",
        "What are the benefits of making incremental changes?",
        "What role does an IDE play in coding?",

        # Chapter 4
        "What is defensive programming?",
        "Why is logging important in production code?",
        "What are metrics, and why are they important?",
        "What is tracing, and how does it help in distributed systems?",
        "What are idempotent systems?",
        "Why is input validation important?",
        "What is the role of configuration management in operable code?",
        "What are the common log levels used in logging?",
        "What are the benefits of using immutable data in production code?",
        "Why should configuration changes be logged and versioned?"
    ],
    "Answer": [
        # Chapter 2
        "Unconscious Incompetence, Conscious Incompetence, Conscious Competence, Unconscious Competence.",
        "Focusing on critical skills and concepts early to build a strong foundation.",
        "It allows engineers to apply theoretical knowledge in practical situations, reinforcing learning.",
        "Timeboxing sets limits on how long to work on a task, preventing overcommitment and encouraging focus.",
        "Research before asking, and ask clear, specific questions.",
        "The feeling of self-doubt despite being competent, common among new engineers.",
        "A cognitive bias where people with limited knowledge overestimate their competence.",
        "By seeking and acting on constructive feedback to continuously improve.",
        "Being aware of gaps in knowledge and actively working to improve.",
        "They allow engineers to practice and experiment with new concepts outside of their job tasks.",

        # Chapter 3
        "The future cost of rework caused by taking shortcuts in development.",
        "A systematic approach to modifying legacy code safely, starting with writing tests for existing behavior.",
        "To reduce technical debt and improve long-term maintainability.",
        "Small, manageable updates that minimize risk while improving the system.",
        "Refactoring only when it adds value and avoids unnecessary complexity.",
        "Frequent commits, descriptive commit messages, and effective branching strategies.",
        "Making changes without consulting the team can lead to fragmented code and conflicts.",
        "To ensure that changes don’t break existing functionality.",
        "Safer updates, better testing, and quicker feedback on changes.",
        "It helps streamline coding, debugging, and navigating large codebases.",

        # Chapter 4
        "Writing code that anticipates and handles potential failures to improve robustness.",
        "It helps monitor and debug systems by providing insights into the system’s behavior.",
        "Metrics measure the performance and health of systems in production, helping to monitor their status.",
        "Tracing tracks the flow of requests through different services, helping identify bottlenecks and failures.",
        "Systems that can handle repeated operations without changing the outcome.",
        "It ensures that inputs are correct, preventing issues downstream in the application.",
        "Configuration should be treated as code, versioned, and tested to ensure reliability in production.",
        "Debug, Info, Warning, Error, and Critical.",
        "It reduces the risk of unintended side effects and ensures data integrity.",
        "To ensure that configuration changes are tracked and can be rolled back if needed."
    ]
}

# Convert the flashcards to a DataFrame for CSV export
flashcards_chapter_2_4_df = pd.DataFrame(flashcards_chapter_2_4)

# Save the flashcards to a CSV file for Anki
csv_file_path = '/mnt/data/flashcards_chapters_2_4_for_anki.csv'
flashcards_chapter_2_4_df.to_csv(csv_file_path, index=False)

csv_file_path