## tutorial
参考  
https://pypi.org/project/mcp/  
https://github.com/codebasics/ai-agents/tree/main/2_mcp_leave_management

```pip install uv```  
```
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```  
```cd [project name]``` 
```uv init [project name]```  
```uv add "mcp[cli]"```  
main.pyを色々する  
```uv run mcp install main.py```    
ここでclaudeを再起動するが、タスクマネジャーからkillしないと反映されないっぽい  
