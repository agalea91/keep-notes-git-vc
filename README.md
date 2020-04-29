# Keep Notes Git VC

Log your Google Keep notes to git version control.

1. Create git repo for your notes and connect it to remote.

```
cd ~/
mkdir "Keep Notes Backup"
cd "Keep Notes Backup"
mkdir notes
git init
git remote add origin <remote_uri>
```

2. Clone repo.

```
cd ~/
git clone https://github.com/agalea91/keep-notes-git-vc.git
cd keep-notes-git-vc
```

3. Modify "notes" volume in `docker-compose.yaml` if needed. Should mount the directory created in step 1.

4. Create App Password for Google account and put info in `.env`.

```
cat > .env
GOOGLE_KEEP_APP_USER=<your_email>@gmail.com
GOOGLE_KEEP_APP_PASS=<app_password>
```

5. Build and run docker image.

```
docker-compose up
```


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


