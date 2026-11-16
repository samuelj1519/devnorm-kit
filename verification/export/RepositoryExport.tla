--------------------------- MODULE RepositoryExport ---------------------------
EXTENDS Naturals, FiniteSets, TLC
CONSTANTS Units, Seed
VARIABLES phase, disk, backup, installed, external, journal, lease, source,
          document, seenDocument, committed
vars == <<phase, disk, backup, installed, external, journal, lease, source,
          document, seenDocument, committed>>
Base(u) == IF u = Seed THEN "absent" ELSE "old"
Active == phase \in {"preflight", "staged", "journal", "replacing", "verified", "recovering"}
Init == /\ phase = "preflight" /\ disk = [u \in Units |-> Base(u)]
        /\ backup = {} /\ installed = {} /\ external = {}
        /\ journal = FALSE /\ lease = TRUE /\ source = TRUE
        /\ document = 0 /\ seenDocument = 0 /\ committed = FALSE
KeepControl == UNCHANGED <<external, journal, lease, source, document, seenDocument, committed>>
Stage == /\ phase = "preflight" /\ lease /\ source /\ external = {}
         /\ phase' = "staged"
         /\ UNCHANGED <<disk, backup, installed>> /\ KeepControl
Journal == /\ phase = "staged" /\ lease /\ source /\ external = {}
           /\ phase' = "journal" /\ journal' = TRUE
           /\ UNCHANGED <<disk, backup, installed, external, lease, source,
                           document, seenDocument, committed>>
MoveOld(u) == /\ phase \in {"journal", "replacing"} /\ lease /\ source
              /\ u \notin backup /\ u \notin installed /\ disk[u] = Base(u)
              /\ disk' = [disk EXCEPT ![u] = "absent"]
              /\ backup' = backup \cup {u} /\ phase' = "replacing"
              /\ UNCHANGED installed /\ KeepControl
Place(u) == /\ phase = "replacing" /\ lease /\ source
            /\ u \in backup /\ u \notin installed /\ disk[u] = "absent"
            /\ disk' = [disk EXCEPT ![u] = "new"]
            /\ installed' = installed \cup {u}
            /\ UNCHANGED <<phase, backup>> /\ KeepControl
Verify == /\ phase = "replacing" /\ lease /\ source
          /\ installed = Units /\ \A u \in Units: disk[u] = "new"
          /\ phase' = "verified"
          /\ UNCHANGED <<disk, backup, installed>> /\ KeepControl
Commit == /\ phase = "verified" /\ lease /\ source
          /\ \A u \in Units: disk[u] = "new"
          /\ phase' = "complete" /\ committed' = TRUE /\ journal' = FALSE
          /\ UNCHANGED <<disk, backup, installed, external, lease, source, document, seenDocument>>
Fail == /\ Active /\ phase # "recovering" /\ phase' = "recovering"
        /\ UNCHANGED <<disk, backup, installed>> /\ KeepControl
SafeRecovery == lease /\ external = {}
                /\ \A u \in Units: disk[u] = IF u \in installed THEN "new"
                                    ELSE IF u \in backup THEN "absent" ELSE Base(u)
Rollback == /\ phase = "recovering" /\ SafeRecovery
            /\ disk' = [u \in Units |-> Base(u)]
            /\ phase' = "restored" /\ journal' = FALSE
            /\ UNCHANGED <<backup, installed, external, lease, source, document, seenDocument, committed>>
Blocked == /\ phase = "recovering" /\ ~SafeRecovery /\ phase' = "blocked"
           /\ UNCHANGED <<disk, backup, installed>> /\ KeepControl
Foreign(u) == /\ Active /\ u \notin external
              /\ disk' = [disk EXCEPT ![u] = "foreign"]
              /\ external' = external \cup {u}
              /\ UNCHANGED <<phase, backup, installed, journal, lease, source, document, seenDocument, committed>>
EditDocument == /\ Active /\ document = 0 /\ document' = 1 /\ seenDocument' = 1
                /\ UNCHANGED <<phase, disk, backup, installed, external, journal, lease, source, committed>>
LoseLease == /\ Active /\ lease /\ lease' = FALSE
             /\ UNCHANGED <<phase, disk, backup, installed, external, journal, source, document, seenDocument, committed>>
ChangeSource == /\ Active /\ source /\ source' = FALSE
                /\ UNCHANGED <<phase, disk, backup, installed, external, journal, lease, document, seenDocument, committed>>
Advance == Stage \/ Journal \/ (\E u \in Units: MoveOld(u) \/ Place(u))
           \/ Verify \/ Commit \/ Fail \/ Rollback \/ Blocked
Terminal == phase \in {"complete", "restored", "blocked"}
Next == Advance \/ (\E u \in Units: Foreign(u)) \/ EditDocument \/ LoseLease \/ ChangeSource
        \/ (Terminal /\ UNCHANGED vars)
Spec == Init /\ [][Next]_vars /\ WF_vars(Advance)
Terminates == <>Terminal
NeverComplete == phase # "complete"
NeverRestoredAfterSeed == ~(phase = "restored" /\ Seed \in installed)
NeverBlockedAfterSeed == ~(phase = "blocked" /\ Seed \in installed /\ Seed \in external)
PreserveForeign == \A u \in external: disk[u] = "foreign"
PreserveDocument == document = seenDocument
RecordedOnlyExact == committed => (phase = "complete" /\ source /\ lease /\ \A u \in Units: disk[u] = "new")
RetainRecoveryEvidence == phase = "blocked" /\ backup # {} => journal
=============================================================================
